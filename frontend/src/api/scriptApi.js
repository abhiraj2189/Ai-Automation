import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export async function generateScript(topic) {
  const response = await API.post("/script/", {
    topic,
  });

  return response.data;
}