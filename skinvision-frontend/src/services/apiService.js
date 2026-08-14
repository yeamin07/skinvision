import axios from "axios";

// const API_BASE_URL = 'http://localhost:8000/api'
const API_URL = "https://skinvision-ewwr.onrender.com";

export const predictSkinDisease = async (imageFile) => {
    const formData = new FormData()
    formData.append('image',imageFile)

    try{
        const response = await axios.post(
            `${API_URL}/api/predict/`,
            formData,
            {
                headers:{
                    'Content-Type': 'multipart/form-data',
                },
            }
        );
        return response.data
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
};



export const healthCheck = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/health/`);
    return response.data;
  } catch (error) {
    console.error('Health Check Error:', error);
    throw error;
  }
};