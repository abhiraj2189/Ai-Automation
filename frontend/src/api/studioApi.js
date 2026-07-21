// frontend/src/api/studioApi.js

import api from "./api";

/*
=========================================
GENERATE AI VIDEO
=========================================
*/

export const generateVideo = async (

    topic,
    language = "English",
    duration = 60

) => {

    const response = await api.post(

        "/studio/generate",

        {

            topic,

            language,

            duration

        }

    );

    return response.data;

};

/*
=========================================
GENERATE FROM CUSTOM SCRIPT
=========================================
*/

export const generateFromScript = async (

    script,
    language = "English"

) => {

    const response = await api.post(

        "/studio/script",

        {

            script,

            language

        }

    );

    return response.data;

};

/*
=========================================
UPLOAD VOICE
=========================================
*/

export const uploadVoice = async (file) => {

    const form = new FormData();

    form.append("file", file);

    const response = await api.post(

        "/studio/upload-voice",

        form,

        {

            headers: {

                "Content-Type": "multipart/form-data"

            }

        }

    );

    return response.data;

};

/*
=========================================
UPLOAD BACKGROUND MUSIC
=========================================
*/

export const uploadMusic = async (file) => {

    const form = new FormData();

    form.append("file", file);

    const response = await api.post(

        "/studio/upload-music",

        form,

        {

            headers: {

                "Content-Type": "multipart/form-data"

            }

        }

    );

    return response.data;

};

/*
=========================================
UPLOAD CUSTOM VIDEO
=========================================
*/

export const uploadVideo = async (file) => {

    const form = new FormData();

    form.append("file", file);

    const response = await api.post(

        "/studio/upload-video",

        form,

        {

            headers: {

                "Content-Type": "multipart/form-data"

            }

        }

    );

    return response.data;

};

/*
=========================================
GET AVAILABLE VOICES
=========================================
*/

export const getVoices = async () => {

    const response = await api.get(

        "/studio/voices"

    );

    return response.data;

};

/*
=========================================
GET PROJECT HISTORY
=========================================
*/

export const getProjects = async () => {

    const response = await api.get(

        "/studio/projects"

    );

    return response.data;

};

/*
=========================================
DELETE PROJECT
=========================================
*/

export const deleteProject = async (id) => {

    const response = await api.delete(

        `/studio/projects/${id}`

    );

    return response.data;

};