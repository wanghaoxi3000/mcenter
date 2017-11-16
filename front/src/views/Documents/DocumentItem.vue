<template>
  <div class="blog-item">
    <h1><router-link :to="itemInfo.url">{{ itemInfo.title }}</router-link></h1>
    <p class="blog-abstract">{{ itemInfo.synopsis }}</p>
    <div class="blog-info">
      <Icon type="bookmark" /> {{ itemInfo.category }}
      &nbsp&nbsp
      <Icon type="ios-clock" /> {{ itemInfo.timestamp }}
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
          url: 'documents/test',
          title: '文章标题',
          synopsis: '文章摘要',
          category: '编程技术',
          timestamp: '1974-02-06 21:09'
        }
      }
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.blog-item{
  margin: 0;
  padding: 0;
  a{
    color: #495060;
  }
  .blog-abstract {
    font-size: 16px;
    margin: 10px 0;
  }
  .blog-info {
    font-size: 13px;
  }
}
</style>
