import api from "./apiClient";

export const analytics=()=>api.get("/analytics");