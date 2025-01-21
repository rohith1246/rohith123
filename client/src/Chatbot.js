import React, { useState, useRef, useEffect } from 'react';
import './Chatbot.css';

const CommonQuestions = [
  "What is your pricing?",
  "I want to sell my property",
  "How can I search for properties?",
  "What documents are required?",
  "How do I contact support?",
  "I want to buy a property"
];

const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { user: 'bot', text: 'Hello! How can I help you today? You can click on common questions below or type your own question.' }
  ]);
  const [userInput, setUserInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const toggleChatbot = () => setIsOpen(!isOpen);

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const resetChat = () => {
    setMessages([
      { user: 'bot', text: 'Hello! How can I help you today?.' }
    ]);
    setUserInput('');
  };

  const handleSendMessage = async (text = userInput.trim()) => {
    if (text) {
      const newMessage = { user: 'user', text };
      setMessages(prev => [...prev, newMessage]);
      setUserInput('');
      setIsLoading(true);

      try {
        const response = await fetch('http://localhost:5000/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ user_input: text }),
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        const botReply = {
          user: 'bot',
          text: data.response || 'Sorry, I didn\'t understand that.'
        };
        setMessages(prev => [...prev, botReply]);
      } catch (error) {
        console.error('Error:', error);
        const botReply = {
          user: 'bot',
          text: 'Sorry, there was an error processing your request.'
        };
        setMessages(prev => [...prev, botReply]);
      } finally {
        setIsLoading(false);
      }
    }
  };

  return (
    <div className="chatbot-container">
      <button 
        className="chatbot-toggle"
        onClick={toggleChatbot}
        aria-label={isOpen ? 'Close chat' : 'Open chat'}
      >
        {isOpen ? 'Close Chat' : 'Chat with us'}
      </button>

      {isOpen && (
        <div className="chatbot-window">
          <div className="chatbot-header">
            <h3>Nextopson Support</h3>
          </div>

          <div className="messages-container">
            {messages.map((msg, index) => (
              <div
                key={`${index}-${msg.user}`}
                className={`message-wrapper ${msg.user === 'user' ? 'user-message' : 'bot-message'}`}
              >
                <div className="message">
                  <p>{msg.text}</p>
                </div>
              </div>
            ))}
            <div ref={messagesEndRef} />
            {isLoading && (
              <div className="message-wrapper bot-message">
                <div className="message">
                  <p>Typing...</p>
                </div>
              </div>
            )}
          </div>

          <div className="chatbot-footer">
            <div className="common-questions">
              {CommonQuestions.map((question, index) => (
                <button
                  key={index}
                  onClick={() => handleSendMessage(question)}
                  disabled={isLoading}
                  className="question-button"
                >
                  {question}
                </button>
              ))}
            </div>
            
            <div className="input-container">
              <input
                type="text"
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Type your message..."
                disabled={isLoading}
                className="chat-input"
              />
              <button
                onClick={() => handleSendMessage()}
                disabled={isLoading || !userInput.trim()}
                className="send-button"
              >
                Send
              </button>
            </div>
            
            <button
              onClick={resetChat}
              className="reset-button"
            >
              Reset Chat
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Chatbot;