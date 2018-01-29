import BlogLayout from '@/views/BaseLayout/BlogLayout.vue'
import BlogIndex from '@/views/BlogIndex/BlogIndex.vue'
import BlogArticle from '@/views/BlogArticle/BlogArticle.vue'
import PageBuilding from '@/views/ErrorPage/PageBuilding.vue'
import Page404 from '@/views/ErrorPage/Page404.vue'

import AdminLayout from '@/views/BaseLayout/AdminLayout.vue'
import AdminIndex from '@/views/AdminIndex/AdminIndex.vue'
import AdminBlogEdit from '@/views/AdminBlogEdit/AdminBlogEdit.vue'

export const pageRouter = [
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
    component: AdminLayout,
    redirect: '/admin/index',
    children: [
      { path: 'index', name: 'adminIndex', component: AdminIndex }
    ]
  },

  { path: '*', redirect: '/404', hidden: true }
]


// 将在Admin侧边栏显示的router
export const sidebarRouter = [
  {
    path: '/admin/blog',
    icon: 'ios-folder',
    name: 'blog-manage',
    title: '博客管理',
    component: AdminLayout,
    children: [
      {
        path: 'edit',
        icon: 'ios-paper-outline',
        name: 'edit-article',
        title: '创建文章',
        component: AdminBlogEdit
      },
      {
        path: 'list',
        icon: 'ios-list-outline',
        name: 'blog-list',
        title: '文章管理',
        component: AdminIndex
      },
    ]
  }
]

export const routers = [
  ...pageRouter,
  ...sidebarRouter,
]
