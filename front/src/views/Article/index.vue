<template>
  <div class="app-container">
    <Row type="flex" justify="center">
      <Col :xs="22" :sm="20" :md="18" :lg="16">
        <h1 class="title">{{title}}</h1>
        <div class="info">
          <Icon type="bookmark" /> {{ category }}
          &nbsp&nbsp
          <Icon type="ios-clock" /> {{ timestamp }}
          <br>
          <article class="markdown-body" v-html="content"></article>
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
.app-container {
  text-align: center;
  .title {
    font-size: 36px;
    margin: 20px;
  }
  .info {
    font-size: 16px;
  }
}
</style>

<style rel="stylesheet/scss" lang="scss">
@import "~github-markdown-css/github-markdown.css";
@import "../../styles/codehilite.css";
.markdown-body {
  text-align: left;
  padding: 45px 15px;
  margin-top: 15px;
  border-top: 1px solid #dddee1;

  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px 0;
    }
  }

  pre {
    background-color: rgba(27, 31, 35, 0.05);
  }
}
</style>
