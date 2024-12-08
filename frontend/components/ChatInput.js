import { useState } from 'react';

export default function ChatInput({ onSendMessage, isLoading, language }) {
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!message.trim() || isLoading) return;

    onSendMessage(message);
    setMessage('');
  };

  const placeholderTexts = {
    'en': 'Ask about crops...',
    'ml': 'വിളകളെക്കുറിച്ച് ചോദിക്കുക...'
  };

  return (
    <form onSubmit={handleSubmit} className="flex mt-4">
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder={placeholderTexts[language] || 'Ask about crops...'}
        disabled={isLoading}
        className="flex-grow p-3 border rounded-l-lg"
      />
      <button
        type="submit"
        disabled={isLoading}
        className="bg-green-500 text-white p-3 rounded-r-lg"
      >
        {isLoading ? 'Processing...' : 'Send'}
      </button>
    </form>
  );
}
