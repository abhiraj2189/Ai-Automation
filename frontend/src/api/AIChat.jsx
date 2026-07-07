const sendMessage = async () => {
  if (!input.trim()) return;

  const userMessage = {
    role: "user",
    text: input,
  };

  setMessages((prev) => [...prev, userMessage]);

  const prompt = input;
  setInput("");

  try {
    const response = await sendMessageAPI(prompt);

    setMessages((prev) => [
      ...prev,
      {
        role: "ai",
        text: response,
      },
    ]);
  } catch (err) {
    console.error(err);

    setMessages((prev) => [
      ...prev,
      {
        role: "ai",
        text: "Error connecting to AI.",
      },
    ]);
  }
};