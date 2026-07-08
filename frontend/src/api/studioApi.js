const API = "http://127.0.0.1:8000";

export async function generateProject(topic) {
  const response = await fetch(`${API}/studio`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      topic,
    }),
  });

  if (!response.ok) {
    throw new Error("Generation Failed");
  }

  return await response.json();
}