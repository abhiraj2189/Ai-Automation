import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export const login = async (email, password) => {
  const response = await API.post("/auth/login", {
    email,
    password,
  });

  return response.data;
};

export const register = async (username, email, password) => {
  const response = await API.post("/auth/register", {
    username,
    email,
    password,
  });

  return response.data;
};

export default API;