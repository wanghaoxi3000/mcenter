<template>
  <div>
    <Table
      stripe
      border
      :loading="false"
      :columns="blogTable"
      :data="data1">
    </Table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      blogTable: [
        {
          type: 'index',
          title: '序号',
          width: 80
        },
        {
          title: '标题',
          key: 'title'
        },
        {
          title: '来源',
          key: 'source',
          width: 100
        },
        {
          title: '类别',
          key: 'category'
        },
        {
          title: '时间戳',
          key: 'time',
          width: 120
        },
        {
          title: '阅读次数',
          key: 'num',
          width: 100
        }
      ],
      data1: [
        {
          title: '博客文章',
          source: '原创',
          category: '类别',
          time: '2018-01-08',
          num: '10'
        },
        {
          title: '博客文章2',
          source: '原创',
          category: '类别',
          time: '2018-01-08',
          num: '10'
        },
        {
          title: '博客文章3',
          source: '原创',
          category: '类别',
          time: '2018-01-08',
          num: '10'
        }
      ]
    }
  }
}
</script>

<style>

</style>
