import Vue from 'vue'
import iView from 'iview'
import Router from 'vue-router'
import { routers } from './router'

Vue.use(Router)

// 路由配置
const RouterConfig = {
  mode: 'history',
  routes: routers
}

const router = new Router(RouterConfig)

router.beforeEach((to, from, next) => {
  iView.LoadingBar.start()
  next()
})

router.afterEach((to) => {
  iView.LoadingBar.finish()
  window.scrollTo(0, 0)
})

export default router
