$(function(){$(document).on("click",".next",function(n){n.preventDefault(),$.scrollTo($("section.blog"),1e3),$("#listing").load(blog_page,next_params,function(){})}),$(document).on("click",".previous",function(n){n.preventDefault(),$.scrollTo($("section.blog"),1e3),$("#listing").load(blog_page,prev_params,function(){})})});