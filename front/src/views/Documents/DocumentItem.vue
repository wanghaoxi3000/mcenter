<template>
  <div>
    <h1>{{ itemInfo.title }}</h1>
    <p class="blog-abstract">{{ itemInfo.synopsis }}</p>
    <div class="blog-info">
      <Icon type="bookmark" /> {{ itemInfo.category }}
      &nbsp&nbsp
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
          time: '1974-02-06 21:09' }
      }
    }
  }
}
</script>

<style scoped>
  .blog-abstract {
    font-size: 16px;
    margin: 10px 0;
  }
  .blog-info {
    font-size: 13px;
  }
</style>
