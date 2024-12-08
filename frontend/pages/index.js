import { useState } from 'react';
import axios from 'axios';
import ChatInput from '../components/ChatInput';
import ChatMessages from '../components/ChatMessages';
import LanguageSelector from '../components/LanguageSelector';

export default function Home() {
  // STATE MANAGEMENT
  const [messages, setMessages] = useState([]);
  const [language, setLanguage] = useState('en'); // DEFAULT LANGUAGE
  const [isLoading, setIsLoading] = useState(false);

  // CHAT SUBMISSION HANDLER
  const handleSendMessage = async (userMessage) => {
    // Create a copy of existing messages and add the user message
    const newMessages = [...messages, { text: userMessage, sender: 'user' }];
    setMessages(newMessages);
    setIsLoading(true);

    try {
      // Extensive logging for debugging
      console.group('Chat Request');
      console.log('Sending Message:', userMessage);
      console.log('Current Language:', language);

      // Axios request with comprehensive configuration
      const response = await axios({
        method: 'post',
        url: 'http://localhost:5000/chat',
        data: {
          message: userMessage,
          language: language
        },
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        timeout: 15000, // 15-second timeout
        validateStatus: function (status) {
          // Reject only if the status code is not in the 200-299 range
          return status >= 200 && status < 300;
        }
      });

      // Log response details
      console.log('Backend Response:', response.data);
      console.log('Response Status:', response.status);
      console.groupEnd();

      // Update messages with bot response
      setMessages([
        ...newMessages,
        { text: response.data.response, sender: 'bot' }
      ]);
    } catch (error) {
      // Comprehensive error logging
      console.group('Chat Error');
      console.error('Error Type:', error.name);
      console.error('Error Message:', error.message);

      // Log more detailed error information
      if (error.response) {
        // The request was made and the server responded with a status code
        console.error('Error Response Data:', error.response.data);
        console.error('Error Response Status:', error.response.status);
        console.error('Error Response Headers:', error.response.headers);
      } else if (error.request) {
        // The request was made but no response was received
        console.error('No response received', error.request);
      } else {
        // Something happened in setting up the request
        console.error('Error Setup:', error.message);
      }
      console.groupEnd();

      // User-friendly error messages
      const errorMessage = error.response?.data?.error || 
                           'Sorry, something went wrong. Please try again.';

      // Update messages with error response
      setMessages([
        ...newMessages,
        { text: errorMessage, sender: 'bot' }
      ]);
    } finally {
      // Ensure loading state is always turned off
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-gray-50 min-h-screen">
      <div className="bg-white shadow-md rounded-lg p-6">
        {/* LANGUAGE SELECTOR */}
        <LanguageSelector
          currentLanguage={language}
          onLanguageChange={setLanguage}
        />
        {/* CHAT MESSAGES DISPLAY */}
        <ChatMessages messages={messages} />
        {/* CHAT INPUT */}
        <ChatInput
          onSendMessage={handleSendMessage}
          isLoading={isLoading}
          language={language}
        />
      </div>
    </div>
  );
}
