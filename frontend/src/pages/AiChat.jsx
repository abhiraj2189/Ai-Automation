import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { sendMessage } from "../api/chatApi";

export default function AIChat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim() || loading) return;

    const userInput = input;

    // User message
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        text: userInput,
      },
    ]);

    setInput("");
    setLoading(true);

    try {
      const aiReply = await sendMessage(userInput);

      setMessages((prev) => [
        ...prev,
        {
          role: "ai",
          text: aiReply,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "ai",
          text: "❌ Unable to connect to AI backend.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <MainLayout>
      <div className="h-[80vh] flex flex-col">

        {/* Chat Messages */}
        <div className="flex-1 overflow-y-auto bg-zinc-900 rounded-xl p-5 space-y-4">

          {messages.length === 0 && (
            <div className="text-center text-zinc-400 mt-10">
              🤖 Ask me anything...
            </div>
          )}

          {messages.map((msg, index) => (
            <div
              key={index}
              className={`max-w-[75%] p-4 rounded-xl ${
                msg.role === "user"
                  ? "bg-cyan-600 ml-auto"
                  : "bg-zinc-700"
              }`}
            >
              {msg.text}
            </div>
          ))}

          {loading && (
            <div className="bg-zinc-700 rounded-xl p-4 w-fit">
              🤖 Thinking...
            </div>
          )}

        </div>

        {/* Input Area */}
        <div className="flex gap-3 mt-4">

          <input
            type="text"
            placeholder="Ask anything..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleSend();
              }
            }}
            className="flex-1 bg-zinc-800 rounded-xl p-4 outline-none"
          />

          <button
            onClick={handleSend}
            disabled={loading}
            className="bg-cyan-500 hover:bg-cyan-600 px-8 rounded-xl transition"
          >
            {loading ? "..." : "Send"}
          </button>

        </div>

      </div>
    </MainLayout>
  );
}