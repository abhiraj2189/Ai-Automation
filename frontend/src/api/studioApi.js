import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 300000,
});

export const generateVideo = async (topic) => {
  const response = await API.post("/studio/", {
    topic,
  });

  return response.data;
};

export default API;