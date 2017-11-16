import axios from 'axios'

// 创建axios实例
const service = axios.create({
  // baseURL: 'https://easy-mock.com/mock/59fd94a56b54331215b423ce',
  baseURL: 'http://localhost:8000',
  timeout: 15000
})

export default service
