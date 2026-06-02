//program to implement activity selection problem
#include <stdio.h>
#include <stdlib.h>
typedef struct Activity{
	int start;
	int end;
}activity;
int compare(const void *x, const void *y){
	return (*(activity*)x).end - (*(activity*)y).end;
}
int main(){
	int n;
	scanf("%d", &n);
	activity activities[n];
	for (int i =0; i<n; i++)
		scanf("%d %d", &activities[i].start,&activities[i].end);
	qsort(activities,n, sizeof(activity),compare);
	printf("{%d, %d} ", activities[0].start, activities[0].end);
	for (int i = 0; i<n; i++){
		for (int j = i+1;j<n;j++){
			if (activities[j].start>=activities[i].end){
				printf("{%d, %d} ", activities[j].start, activities[j].end);
				i = j;
			}
		}
	}
	return 0;
}