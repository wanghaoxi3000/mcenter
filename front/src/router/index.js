import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/Layout/Layout'
import Documents from '@/views/Documents'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Layout',
      component: Layout,
      redirect: '/documents',
      children: [
        { path: 'documents', component: Documents }
      ]
    }
  ]
})
