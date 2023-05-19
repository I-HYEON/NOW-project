<template>
  <div>
    맞춤형 상품 추천

    <table border="1">
        <th>선택</th>
        <tr>
            <td>성별</td>
            <td>
                <input type="radio" name="tendency" v-model="tendency" value="1">여자
                <input type="radio" name="tendency" v-model="tendency" value="2">남자
            </td>
        </tr>
        <tr>
            <td>나이</td>
            <td>
                <input type="radio" name="tendency" v-model="tendency" value="1">20세 이하
                <input type="radio" name="tendency" v-model="tendency" value="2">20세 ~ 29세
                <input type="radio" name="tendency" v-model="tendency" value="3">30세 ~ 40세
                <input type="radio" name="tendency" v-model="tendency" value="4">40세 ~ 49세
                <input type="radio" name="tendency" v-model="tendency" value="5">50세 ~ 59세
            </td>
        </tr>
        <tr>
            <td>연봉</td>
            <td>
                <input type="radio" name="tendency" v-model="tendency" value="1">1000만원 ~ 2000만원
                <input type="radio" name="tendency" v-model="tendency" value="2">2000만원 ~ 3000만원
                <input type="radio" name="tendency" v-model="tendency" value="3">3000만원 ~ 4000만원
                <input type="radio" name="tendency" v-model="tendency" value="4">4000만원 ~ 5000만원
                <input type="radio" name="tendency" v-model="tendency" value="5">5000만원 ~ 6000만원
            </td>
        </tr>
        <tr>
            <td>자산</td>
            <td>
                <input type="radio" name="tendency" v-model="tendency" value="1">1000만원 ~ 2000만원
                <input type="radio" name="tendency" v-model="tendency" value="2">2000만원 ~ 3000만원
                <input type="radio" name="tendency" v-model="tendency" value="3">3000만원 ~ 4000만원
                <input type="radio" name="tendency" v-model="tendency" value="4">4000만원 ~ 5000만원
                <input type="radio" name="tendency" v-model="tendency" value="5">5000만원 ~ 6000만원
            </td>
        </tr>
        <tr>
            <td>저축성향</td>
            <td>
                <input type="radio" name="tendency" v-model="tendency" value="1">단기
                <input type="radio" name="tendency" v-model="tendency" value="2">중기
                <input type="radio" name="tendency" v-model="tendency" value="3">장기
            </td>
        </tr>
    </table>
  </div>

</template>

<script>
export default {
    name: 'Recommend'
}
</script>

<style>

</style>