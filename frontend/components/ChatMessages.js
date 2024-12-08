// ChatMessages.js
import React from 'react';

export default function ChatMessages({ messages }) {
  return (
    <div className="mb-4 space-y-2">
      {messages.map((message, index) => (
        <div 
          key={index} 
          className={`p-3 rounded-lg ${
            message.sender === 'user' 
              ? 'bg-blue-100 text-right' 
              : 'bg-green-100 text-left'
          }`}
        >
          {message.text}
        </div>
      ))}
    </div>
  );
}