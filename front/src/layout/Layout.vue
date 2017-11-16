<template>
    <div class="layout">
        <Menu mode="horizontal" theme="dark" active-name="1">
            <div class="layout-nav">
              <router-link to="/documents">
                <MenuItem name="1">
                    <Icon type="chatbubble-working"></Icon>
                    文章
                </MenuItem>
              </router-link>
                <MenuItem name="2">
                    <Icon type="document-text"></Icon>
                    资讯
                </MenuItem>
                <MenuItem name="3">
                    <Icon type="ios-information"></Icon>
                    关于
                </MenuItem>
            </div>
        </Menu>

        <router-view></router-view>

        <div class="bottom">
          <img src="../assets/logo.png" class="layout-logo" alt="某中二的黑科技研究中心">
          <div class="layout-copy">某中二的黑科技研究中心</div>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.layout {
  border: 1px solid #d7dde4;

  .layout-nav {
    display: table;
    margin: 0 auto;

    & menuitem {
      display: table-cell;
    }
  }

  .bottom {
    border-top-style: solid;
    border-top-width: 1px;
    border-top-color: #d7dde4;
    padding: 10px 0;

    .layout-logo {
      max-width: 300px;
      width: 60%;
      height: auto;
      display: block;
      margin: 0 auto;
    }
    .layout-copy {
      text-align: center;
      padding: 10px;
      color: #9ea7b4;
      cursor: default;
    }
  }
}
</style>
