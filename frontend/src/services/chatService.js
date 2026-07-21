import api from "./apiClient";

export const askAI=(message)=>

api.post("/chat",{

message

});