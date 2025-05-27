import axiosInstance from './axiosInstance';


export async function searchProducts(product) {
    const res = await fetch("http://localhost:8000/search?product=Charizard", {
  method: "GET",
  headers: {
    "x-api-key": "Pancopinco",
  },
})}

export async function getUserInfo(username) {
  const res = await axiosInstance.get(`/user`, {
    params: { username }
  });
  return res.data;
}

export async function getOrders() {
  const res = await axiosInstance.get('/orders');
  return res.data;
}