<template>
  <div>
    <router-link :to="{
      name: 'ArticleDetailView',
      params: {id: article.id }}">
    <p>{{ article.title }}</p>
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>
