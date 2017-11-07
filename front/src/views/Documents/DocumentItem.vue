<template>
  <div>
    <h1>{{ itemInfo.title }}</h1>
    <p>{{ itemInfo.synopsis }}</p>
    <div>
      <Icon type="pricetag" />{{ itemInfo.category }}
      <Icon type="ios-clock" /> {{ itemInfo.time }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    itemInfo: {
      type: Object,
      default() {
        return {
          title: '文章标题',
          synopsis: '文章摘要',
          category: '编程技术',
          time: '1974-02-06 21:09:45' }
      }
    }
  }
}
</script>

<style>

</style>
