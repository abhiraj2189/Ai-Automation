import { useState } from "react";
import MainLayout from "../layouts/MainLayout";

export default function AIChat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input) return;

    const userMessage = { role: "user", text: input };
    setMessages([...messages, userMessage]);

    setInput("");

    // dummy AI response (backend connect later)
    setTimeout(() => {
      const botMessage = {
        role: "ai",
        text: "🤖 AI response coming soon...",
      };
      setMessages((prev) => [...prev, botMessage]);
    }, 500);
  };

  return (
    <MainLayout>
      <div className="h-[80vh] flex flex-col">

        {/* Messages */}
        <div className="flex-1 overflow-auto space-y-3 p-4 bg-zinc-900 rounded-xl">

          {messages.map((msg, i) => (
            <div
              key={i}
              className={`p-3 rounded-lg w-fit max-w-[70%] ${
                msg.role === "user"
                  ? "bg-cyan-600 ml-auto"
                  : "bg-zinc-700"
              }`}
            >
              {msg.text}
            </div>
          ))}

        </div>

        {/* Input */}
        <div className="flex gap-3 mt-4">

          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask AI..."
            className="flex-1 p-3 rounded-lg bg-zinc-800 outline-none"
          />

          <button
            onClick={sendMessage}
            className="bg-cyan-500 px-6 py-2 rounded-lg"
          >
            Send
          </button>

        </div>

      </div>
    </MainLayout>
  );
}