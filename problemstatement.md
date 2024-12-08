# Multilingual Agriculture Chatbot  

## **Problem Statement**  
- Farmers and agriculture stakeholders often face challenges in accessing reliable and localized crop-related information in their native language.  
- This project aims to address these challenges by developing a Malayalam-supporting chatbot capable of answering queries about crops, fertilizers, pest control, and modern agricultural practices.  
- Additionally, the chatbot provides information on **state and central government agricultural schemes**, advice on the right **food and nutrition for farm animals** like cows and pigs, and guidance on **identifying and managing pests or creatures harmful to crops**.  
- By offering a comprehensive knowledge base, the chatbot empowers farmers with localized, actionable insights to improve their productivity and sustainability.  

## **Solution**  
The solution involves developing a **Multilingual Agriculture Chatbot** using a custom **fine-tuned quantized LLaMA3.2 model** for intelligent responses in **Malayalam**. The chatbot will provide:  
1. **Localized Crop Information**: Insights on cultivation practices, pest control, fertilizers, and modern techniques.  
2. **Government Schemes**: State and central government schemes tailored to farmers' needs.  
3. **Animal Care**: Recommendations for proper nutrition and feeding practices for farm animals like cows and pigs.  
4. **Pest Management**: Identifying harmful creatures affecting crops and offering preventive measures.  

## **Technical Approach**  
1. **Frontend**: Built with **Next.js** for an interactive and user-friendly experience.  
2. **Backend**: Developed using **Flask** for handling requests and model inference.  
3. **Model**: A custom fine-tuned **Quantized LLaMA3.2 model** for generating responses in Malayalam.  
4. **Pipeline**: Translation of Malayalam input to English, processing with the model, and translating the response back to Malayalam.  
5. **Deployment**: Hosted on a cloud platform (e.g., AWS, Google Cloud, or Azure) for seamless accessibility.

## **Colab link**  
https://colab.research.google.com/drive/1bgRp-6g_S1AxkKVucKoKm1v1UABot7U2?usp=sharing
