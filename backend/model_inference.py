import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ModelHandler:
    def __init__(self, model_path):
        try:
            # Validate model path
            if not os.path.exists(model_path):
                raise ValueError(f"Model path does not exist: {model_path}")

            logger.info(f"Loading model from: {model_path}")
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(model_path)
            
            # Load model with error handling
            self.model = AutoModelForCausalLM.from_pretrained(
                model_path,
                device_map='auto',
                torch_dtype=torch.float16,
                low_cpu_mem_usage=True,
                trust_remote_code=True  # Add this for custom models
            )
            
            # Create pipeline with additional parameters
            self.pipe = pipeline(
                task="text-generation", 
                model=self.model, 
                tokenizer=self.tokenizer, 
                max_length=1024,
                num_return_sequences=1
            )
            
            # Improved prompt template
            self.input_prompt = """### Instruction:
You are a helpful AI assistant. Provide a concise and informative response to the following query.

### Input:
{0}

### Response:"""
            
            logger.info("Model loaded successfully")
        
        except Exception as e:
            logger.error(f"Model initialization error: {e}")
            raise

    def generate_response(self, prompt, language='en'):
        try:
            logger.info(f"Generating response for prompt: {prompt}")
            
            # Format prompt with template
            formatted_prompt = self.input_prompt.format(prompt)
            
            # Generate response with more controlled parameters
            result = self.pipe(
                formatted_prompt, 
                max_new_tokens=150,  # Limit response length
                temperature=0.2,     # More focused responses
                top_p=0.9,           # Nucleus sampling
                num_return_sequences=1
            )
            
            # Extract and clean response
            generated_text = result[0]['generated_text']
            response = generated_text.split('### Response:')[-1].strip()
            
            logger.info("Response generated successfully")
            return response

        except Exception as e:
            logger.error(f"Response generation error: {e}")
            return f"I apologize, but I couldn't process your request. {str(e)}"

MODEL_PATH = r'E:\Data science\001 GenAI\LLM project ConvaAI\Agricultural chatbot\model\final_weights_new'
model_handler = ModelHandler(MODEL_PATH)

def generate_response(message, language='en'):
    return model_handler.generate_response(message, language)