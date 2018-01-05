import Vue from 'vue'
import Router from 'vue-router'
import BlogLayout from '@/views/BaseLayout/BlogLayout.vue'
import BlogIndex from '@/views/BlogIndex/BlogIndex.vue'
import BlogArticle from '@/views/BlogArticle/BlogArticle.vue'
import PageBuilding from '@/views/ErrorPage/PageBuilding.vue'
import Page404 from '@/views/ErrorPage/Page404.vue'

import AdminLayout from '@/views/BaseLayout/AdminLayout.vue'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/404', name: '404', component: Page404 },
    {
      path: '/',
      name: 'Layout',
      component: BlogLayout,
      redirect: '/documents',
      children: [
        { path: 'documents/(page/)?:page(\\d+)?/', name: 'blog', component: BlogIndex, alias: '/' },
        { path: 'documents/:slug', name: 'article', component: BlogArticle }
      ]
    },
    {
      path: '/news',
      component: BlogLayout,
      redirect: '/news/index',
      children: [
        { path: 'index', name: 'newsBoard', component: PageBuilding }
      ]
    },
    {
      path: '/about',
      component: BlogLayout,
      redirect: '/about/index',
      children: [
        { path: 'index', name: 'aboutMe', component: PageBuilding }
      ]
    },

    {
      path: '/admin',
      component: AdminLayout
    },

    { path: '*', redirect: '/404', hidden: true }
  ]
})
