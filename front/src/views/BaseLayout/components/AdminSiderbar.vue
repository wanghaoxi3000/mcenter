<template>
  <Menu
    ref="sideMenu"
    :open-names="openNames"
    :theme="menuTheme"
    width="auto"
    @on-select="changeMenu">

    <template v-for="item in menuList">
      <MenuItem
        v-if="item.children.length<1"
        :name="item.children[0].name"
        :key="'menuitem' + item.name">
        <Icon
          :type="item.icon"
          :size="iconSize"
          :key="'menuicon' + item.name">
        </Icon>
        <span class="layout-text" :key="item.path">{{ item.title }}</span>
      </MenuItem>

      <Submenu v-if="item.children.length >= 1" :name="item.name" :key="item.path">
        <template slot="title">
          <Icon :type="item.icon" :size="iconSize"></Icon>
          <span class="layout-text">{{ item.title }}</span>
        </template>

        <template v-for="child in item.children">
          <MenuItem :name="child.name" :key="'menuitem' + child.name">
          <Icon :type="child.icon" :size="iconSize" :key="'icon' + child.name"></Icon>
          <span class="layout-text" :key="'title' + child.name">{{ child.title }}</span>
          </MenuItem>
        </template>
      </Submenu>
    </template>
  </Menu>
</template>

<script>
export default {
  name: 'sidebarMenu',
  props: {
    menuList: Array,
    iconSize: Number,
    menuTheme: {
      type: String,
      default: 'dark'
    },
    openNames: {
      type: Array
    }
  },
  updated() {
    this.$nextTick(() => {
      if (this.$refs.sideMenu) {
        this.$refs.sideMenu.updateOpened()
      }
    })
  },
  methods: {
    changeMenu(active) {
      this.$emit('on-change', active)
    }
  }
}
</script>

<style scoped>
.ivu-shrinkable-menu{
    height: 100%;
    width: 100%;
}
</style>
