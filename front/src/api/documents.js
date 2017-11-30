import fetch from '@/utils/fetch'

// 获取文章列表
export function articles(page, category, archive) {
  return fetch({
    url: '/blog/articles/',
    method: 'get',
    params: { page, category, archive }
  })
}

// 获取文章详情
export function articleDetail(slug) {
  return fetch({
    url: `/blog/articles/${slug}/`,
    method: 'get'
  })
}

// 获取博文类别列表
export function categories() {
  return fetch({
    url: `/blog/category/`,
    method: 'get'
  })
}

// 获取博文归档数据
export function archives() {
  return fetch({
    url: `/blog/articles/date-archive/`,
    method: 'get'
  })
}
