import fetch from '@/utils/fetch'

// 获取文章列表
export function articles() {
  return fetch({
    url: 'articles',
    method: 'get'
  })
}
