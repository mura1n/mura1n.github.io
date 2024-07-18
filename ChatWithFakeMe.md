---
layout: inner
title: Chat with AI Ellen
permalink: /Chatbot/
---

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChatGPT Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .chat-container {
            width: 400px;
            height: 600px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }
        .chat-header {
            background-color: #007bff;
            color: #fff;
            padding: 15px;
            text-align: center;
            font-size: 1.2em;
        }
        .chat-messages {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            border-bottom: 1px solid #ddd;
        }
        .chat-message {
            display: flex;
            align-items: flex-end;
            margin-bottom: 15px;
        }
        .chat-message.user {
            justify-content: flex-end;
        }
        .chat-message.bot {
            justify-content: flex-start;
        }
        .chat-bubble {
            max-width: 70%;
            padding: 10px;
            border-radius: 10px;
            position: relative;
        }
        .chat-bubble.user {
            background-color: #007bff;
            color: #fff;
            border-bottom-right-radius: 0;
        }
        .chat-bubble.bot {
            background-color: #e5e5ea;
            color: #000;
            border-bottom-left-radius: 0;
        }
        .chat-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin: 0 10px;
        }
        .chat-footer {
            display: flex;
            border-top: 1px solid #ddd;
            padding: 10px;
            background-color: #f9f9f9;
        }
        .chat-input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .chat-send-button {
            background-color: #007bff;
            color: #fff;
            border: none;
            padding: 10px 15px;
            margin-left: 10px;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">ChatGPT Chatbot</div>
        <div class="chat-messages" id="chatMessages"></div>
        <div class="chat-footer">
            <input type="text" id="chatInput" class="chat-input" placeholder="Type a message...">
            <button class="chat-send-button" onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        const chatMessages = document.getElementById('chatMessages');
        const chatInput = document.getElementById('chatInput');

        async function sendMessage() {
            const userMessage = chatInput.value.trim();
            if (!userMessage) return;

            // Display user message
            displayMessage(userMessage, 'user');
            chatInput.value = '';

            // Simulate bot response (replace with actual API call)
            const botResponse = await getBotResponse(userMessage);
            displayMessage(botResponse, 'bot');
        }

        function displayMessage(message, sender) {
            const messageElement = document.createElement('div');
            messageElement.classList.add('chat-message', sender);

            const bubbleElement = document.createElement('div');
            bubbleElement.classList.add('chat-bubble', sender);
            bubbleElement.innerText = message;

            const avatarElement = document.createElement('img');
            avatarElement.classList.add('chat-avatar');
            avatarElement.src = sender === 'user' ? 'https://via.placeholder.com/40?text=U' : 'https://via.placeholder.com/40?text=B';

            if (sender === 'user') {
                messageElement.appendChild(bubbleElement);
                messageElement.appendChild(avatarElement);
            } else {
                messageElement.appendChild(avatarElement);
                messageElement.appendChild(bubbleElement);
            }

            chatMessages.appendChild(messageElement);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        async function getBotResponse(userMessage) {
            // Replace with actual API call to ChatGPT
            const response = await fetch('https://api.yourchatgptbackend.com/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: userMessage })
            });

            const data = await response.json();
            return data.reply;
        }
    </script>
</body>
</html>