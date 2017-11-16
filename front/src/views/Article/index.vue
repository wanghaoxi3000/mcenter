<template>
  <div class="blog-article">
    <Row type="flex" justify="center">
      <Col :xs="22" :sm="18" :md="14" :lg="12">
        <h1 class="title">{{title}}</h1>
        <div class="info">
          <Icon type="bookmark" /> {{ category }}
          &nbsp&nbsp
          <Icon type="ios-clock" /> {{ timestamp }}
          <br>
          <div class="body" v-html="content"></div>
        </div>
      </Col>
    </Row>
  </div>
</template>

<script>
import { articleDetail } from '../../api/documents'

export default {
  data() {
    return {
      title: '正文标题',
      category: '文章类别',
      timestamp: '2017-11-16 11:51',
      content: ''
    }
  },
  created() {
    this.fetchArticle()
  },
  methods: {
    async fetchArticle() {
      const { data } = await articleDetail(this.$route.params.slug)
      this.title = data.title
      this.category = data.category
      this.timestamp = data.timestamp
      this.content = data.html
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.blog-article {
  text-align: center;
  .title {
    font-size: 36px;
    margin: 20px;
  }
  .info {
    font-size: 16px;
  }
  .body {
    font-size: 18px;
    text-align: left;
  }
}
</style>
