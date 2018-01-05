<template>
  <div :style="{background: bgColor}" class="ivu-shrinkable-menu">
    <slot name="top"></slot>
    <AdminSiderbar
      v-show="!shrink"
      :menu-theme="theme"
      :menu-list="menuList"
      :open-names="openNames"
      @on-change="handleChange">
    </AdminSiderbar>
    <AdminSiderbarShrink
      v-show="shrink"
      :menu-theme="theme"
      :menu-list="menuList"
      :icon-color="shrinkIconColor"
      @on-change="handleChange">
    </AdminSiderbarShrink>
  </div>
</template>

<script>
import AdminSiderbar from './AdminSiderbar.vue'
import AdminSiderbarShrink from './AdminSiderbarShrink.vue'
import util from '@/utils'

export default {
  name: 'shrinkableMenu',
  components: {
    AdminSiderbar,
    AdminSiderbarShrink
  },
  props: {
    shrink: {
      type: Boolean,
      default: false
    },
    menuList: {
      type: Array,
      required: true
    },
    theme: {
      type: String,
      default: 'dark',
      validator(val) {
        return util.oneOf(val, ['dark', 'light'])
      }
    },
    beforePush: {
      type: Function
    },
    openNames: {
      type: Array
    }
  },
  computed: {
    bgColor() {
      return this.theme === 'dark' ? '#495060' : '#fff'
    },
    shrinkIconColor() {
      return this.theme === 'dark' ? '#fff' : '#495060'
    }
  },
  methods: {
    handleChange(name) {
      let willpush = true
      if (this.beforePush) {
        if (!this.beforePush(name)) {
          willpush = false
        }
      }
      if (willpush) {
        this.$router.push({
          name: name
        })
      }
      this.$emit('on-change', name)
    }
  }
}
</script>

<style scoped>
.ivu-shrinkable-menu {
  height: 100%;
  width: 100%;
}
</style>
