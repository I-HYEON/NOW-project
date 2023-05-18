<template>
  <tr>
    <th scope="row">{{table.intr_rate_type_nm}}</th>
    <td>{{table.save_trm}}</td>
    <td>{{table.intr_rate}}</td>
    <td>{{table.intr_rate2}}</td>
  </tr>
</template>

<script>
export default {
name: 'Table',
props: {
  table: Object
},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
      