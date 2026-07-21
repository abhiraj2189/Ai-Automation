import api from "./apiClient";

export const getProjects=()=>api.get("/projects");

export const createProject=(data)=>

api.post("/projects",data);

export const deleteProject=(id)=>

api.delete(`/projects/${id}`);