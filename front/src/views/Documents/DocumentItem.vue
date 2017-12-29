<template>
  <div class="blog-item">
    <h1><router-link class="text-link" :to="{name: 'article', params: {slug: itemInfo.slug}}">{{ itemInfo.title }}</router-link></h1>
    <p class="blog-abstract" v-html="itemInfo.synopsis"></p>
    <div class="blog-info">
      <Icon type="bookmark" />
      <router-link class="text-link" :to="{name: 'blog', query: { category: itemInfo.categorySlug }}">
        {{ itemInfo.category }}
      </router-link>
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
          slug: '',
          title: '',
          synopsis: '',
          category: '',
          timestamp: ''
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
  .blog-abstract {
    font-size: 16px;
    margin: 10px 0;
  }
  .blog-info {
    font-size: 13px;
  }
}
</style>
