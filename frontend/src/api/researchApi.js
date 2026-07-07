import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export async function research(topic) {
  const response = await API.post("/research/", {
    topic,
  });

  return response.data;
}