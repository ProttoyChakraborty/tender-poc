chat_container_style = """
        <style>
        .element-container:has(.stChatInput) {
            position: fixed;
            left: 50%;
            bottom: 20px;
            transform: translate(-50%, -50%);
            margin: 0 auto;
            z-index: 1000;
        }
        .stChatInput {
            flex-wrap: nowrap;
        }
        .json-response {
            background-color: rgba(38, 39, 48, 0.5);
            border-radius: 0.5rem;
            padding: 10px;
            margin-top: 10px;
        }
        .json-key {
            color: #ff6c6c;
            font-weight: bold;
            font-style: italic;
        }
        .json-value {
            color: #fafafa;
        }
        .json-list {
            margin-left: 20px;
        }
        </style>
    """