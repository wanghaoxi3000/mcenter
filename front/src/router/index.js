import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/Layout/Layout'
import Documents from '@/views/Documents'
import Article from '@/views/Article'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Layout',
      component: Layout,
      redirect: '/documents',
      children: [
        { path: 'documents/(page/)?:page(\\d+)?/', name: 'blog', component: Documents, alias: '/' },
        { path: 'documents/:slug', name: 'article', component: Article }
      ]
    }
  ]
})
