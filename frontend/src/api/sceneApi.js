import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export async function generateScene(script) {

  const response = await API.post("/scene/", {
    script,
  });

  return response.data;

}