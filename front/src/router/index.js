import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/Layout/Layout'
import Documents from '@/views/Documents'
import Article from '@/views/Article'
import Building from '@/views/Building'
import page404 from '@/views/errorPage/404.vue'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/404', name: '404', component: page404 },
    {
      path: '/',
      name: 'Layout',
      component: Layout,
      redirect: '/documents',
      children: [
        { path: 'documents/(page/)?:page(\\d+)?/', name: 'blog', component: Documents, alias: '/' },
        { path: 'documents/:slug', name: 'article', component: Article }
      ]
    },
    {
      path: '/news',
      component: Layout,
      redirect: '/news/index',
      children: [
        { path: 'index', name: 'newsBoard', component: Building }
      ]
    },
    {
      path: '/about',
      component: Layout,
      redirect: '/about/index',
      children: [
        { path: 'index', name: 'aboutMe', component: Building }
      ]
    },

    { path: '*', redirect: '/404', hidden: true }
  ]
})
