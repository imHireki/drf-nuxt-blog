<template>
  <div class="w-1/2 mx-auto my-20">

    <h1 class="text-3xl font-semibold text-red-600">
      {{ blogTitle }}
    </h1>

    <div v-if="articleList != []">
      <article class="my-20" v-for="article in articleList" :key="article.id">
        <h2 class="text-5xl font-semibold mb-5">{{ article.title }}</h2>
        <p class="mb-5">{{ article.summary }}</p>
        <p class="text-red-500">Read more</p>
      </article>
    </div>

  </div>
</template>

<script>
export default {
  data () {
    return {
      blogTitle: "Test Nuxt Blog",
      articleList: [],
    }
  },

  created() {
    this.loadArticleList();
  },

  methods: {
    loadArticleList() {
      this.$axios

        .$get("http://localhost:8000/api/v1/article/")

        .then((response) => {
          this.articleList = response 
        })
        .catch((error => {
          this.articleList = []
        }));
    }
  },
}
</script>