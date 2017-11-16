import fetch from '@/utils/fetch'

// 获取文章列表
export function articles(page = 1) {
  return fetch({
    url: '/articles/',
    method: 'get',
    params: { page }
  })
}

// 获取文章详情
export function articleDetail(slug) {
  return fetch({
    url: `/articles/${slug}/`,
    method: 'get'
  })
}
