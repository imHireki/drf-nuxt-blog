<template>
  <h1 class="text-3xl font-semibold text-red-600">
    {{ blogTitle }}
  </h1>
</template>
<script>
export default {
  data () {
    return {
      blogTitle: "Test Nuxt Blog",
      articleList: [],
    }
  },
}
</script>