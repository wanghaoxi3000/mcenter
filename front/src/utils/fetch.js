import axios from 'axios'

// 从环境变量中获取API_ROOT
const serverURL = process.env.API_ROOT

// 创建axios实例
const service = axios.create({
  baseURL: serverURL,
  timeout: 15000
})

export default service
