<template>
  <div class="item-list">
    <h3 class="list-title">{{ title }}</h3>
    <div class="list-body">
      <p class="list-item" v-for="(item, index) in items" :key="index" @click="selected(index)">
        {{ item }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: ''
    },
    items: {
      type: Array,
      default() {
        return []
      }
    }
  },
  methods: {
    selected(index) {
      this.$emit('select', index)
    }
  }
}
</script>

<style  rel="stylesheet/scss" lang="scss" scoped>
$container-height: 300px;
$title-height: 26px;
$body-height: $container-height - $title-height;

.item-list {
  margin: 20px 0px;
  max-height: $container-height;
  border: 1px solid #657180;

  .list-title{
    height: $title-height;
    line-height: $title-height;
    cursor: default;
    padding-left: 2px;
    border-bottom: 1px solid #9ea7b4;
  }

  .list-body {
    max-height: $body-height;
    overflow: auto;

    .list-item {
      padding: 2px 8px;
      cursor: pointer;

      &:hover {
        color: #5cadff;
      }

      &:active {
        color: #3091f2;
      }
    }
  }
}
</style>
