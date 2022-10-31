<template>
	<button class="green-btn" type="button">
		<slot></slot>
	</button>
</template>



<script>
export default {
	name: 'green-button'
}
</script>



<style scoped>
.green-btn {
	margin-top: 15px;
	padding: 10px 15px;
	background: none;
	color: teal;
	border: 1px solid teal;
	align-self: flex-end;
} 
</style>