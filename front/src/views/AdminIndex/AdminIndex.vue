<template>
  <div>
    <TableArticle
      :columnsList="blogTable"
      :value="tableData"
      :valueNum="valueCount"
      :loading="loading">
    </TableArticle>
  </div>
</template>

<script>
import { articles } from '../../api/documents'
import TableArticle from './components/TableArticle'

export default {
  components: {
    TableArticle
  },
  data() {
    return {
      loading: false,   // 表格等待标致
      tableData: [],    // 表格数据
      valueCount: 0,    // 数据总数
      blogTable: [      // 表格列数据
        {
          type: 'selection',
          width: 60,
          align: 'center'
        },
        {
          type: 'index',
          align: 'center',
          title: '序号',
          width: 70
        },
        {
          title: '标题',
          key: 'title',
          ellipsis: true
        },
        {
          title: '来源',
          align: 'center',
          key: 'own',
          width: 100
        },
        {
          title: '类别',
          align: 'center',
          key: 'category',
          width: 160
        },
        {
          title: '时间戳',
          align: 'center',
          key: 'timestamp',
          width: 140
        },
        {
          title: '阅读次数',
          align: 'center',
          key: 'readNum',
          width: 100
        },
        {
          title: '操作',
          align: 'center',
          width: 120,
          key: 'handle',
          handle: ['delete']
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
  },
  created() {
    this.fetchData()
  },
  methods: {
    // 获取博客列表数据
    async fetchData() {
      this.loading = true
      const { data } = await articles(10)
      this.valueCount = data.count
      this.tableData = data.results.map(item => {
        if (item.hasOwnProperty('own')) {
          item.own = item.own ? '原创' : '转载'
        }
        return item
      })
      this.loading = false
    }
  }
}
</script>

<style>

</style>
