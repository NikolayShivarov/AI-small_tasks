#include <iostream>
#include <math.h>
#include <vector>
#include <queue>
#include <cstdlib>
#include <algorithm>
using namespace std;

class Configuration{
public:
int numberOfObjects;
vector<bool> in;
int price;

Configuration(int n,vector<bool> a){
   numberOfObjects=n;
   in.resize(n);
   for(int i=0;i<n;i++){
    in[i]=a[i];
  }
}

Configuration(int n){
numberOfObjects=n;
   in.resize(n);
   for(int i=0;i<n;i++){
    in[i]=rand()%2;
  }
  price=0;

}
Configuration(){
}

void operator=(Configuration& other){
   numberOfObjects=other.numberOfObjects;
   in.resize(numberOfObjects);
   for(int i=0;i<numberOfObjects;i++){
    in[i]=other.in[i];
  }
  price=other.price;
}

void mutate(){
  int a=rand()%numberOfObjects;
  in[a]= !in[a];
}


};

Configuration cross(Configuration first,Configuration second){
int n=first.numberOfObjects;
Configuration result(n);
for(int i=0;i<n/2;i++){
result.in[i]=first.in[i];
}
for(int i=n/2;i<n;i++){
result.in[i]=second.in[i];
}
return result;
}

bool operator<(Configuration first,Configuration second){
 return first.price<second.price;

}

void swap(Configuration& first,Configuration& second){
  Configuration c(first.numberOfObjects);
  c=first;
  first=second;
  second=c;

}

void Sort(vector<Configuration>& p){
   for(int i=0;i<p.size();i++){
    for(int j=i+1;j<p.size();j++){
        if(p[j]<p[i]) swap(p[i],p[j]);
    }
   }

}






class Knapsack{
public:
int capacity;
int numberOfObjects;
vector<int> price;
vector<int> weight;

Knapsack(int c,int n,vector<int>& p,vector<int>& w){
  capacity=c;
  numberOfObjects=n;
  price.resize(n);
  weight.resize(n);
  for(int i=0;i<n;i++){
    price[i]=p[i];
    weight[i]=w[i];
  }

}

int calculatePrice(Configuration& c){
    int sum=0;
    for(int i=0;i<numberOfObjects;i++){
        if(c.in[i]) sum+=price[i];
    }
    c.price=sum;
    return sum;
}

int calculateWeight(Configuration& c){
    int sum=0;
    for(int i=0;i<numberOfObjects;i++){
        if(c.in[i]) sum+=weight[i];
    }
    return sum;
}

bool isNotHeavy(Configuration& c){
  if(calculateWeight(c)<=capacity) return true;
  return false;
}

void solve(){
vector<Configuration> population;
population.resize(10);
for(int i=0;i<10;i++){
    bool ready=false;

    while(!ready){
        Configuration c(numberOfObjects);
        calculatePrice(c);
        if(isNotHeavy(c)){
            population[i]=c;
            ready=true;
         }
      }

   }
   Sort(population);
   for(int i=0;i<10;i++){
    cout<<i<<"th: "<<population[i].price<<endl;
   }
   cout<<"-1th generation: "<<population[0].price<<"   "<<population[9].price<<endl;

   for(int i=0;i<201;i++){
    int pos1=rand()%5;
    int pos2=pos1;
    while(pos2==pos1){
        pos2=rand()%5;
    }
    pos1+=5;
    pos2+=5;
    Configuration c1= cross(population[pos1],population[pos2]);
    Configuration c2= cross(population[pos2],population[pos1]);
    c1.mutate();
    c2.mutate();
    calculatePrice(c1);
    calculatePrice(c2);
    if(isNotHeavy(c1) && population[0]<c1) population[0]=c1;
    if(isNotHeavy(c2) && population[1]<c2) population[1]=c2;
    Sort(population);
    if(i==0) cout<<"0th generation: "<<population[0].price<<"   "<<population[9].price<<endl;
    if(i==20) cout<<"20th generation: "<<population[0].price<<"   "<<population[9].price<<endl;
    if(i==50) cout<<"50th generation: "<<population[0].price<<"   "<<population[9].price<<endl;
    if(i==100) cout<<"100th generation: "<<population[0].price<<"   "<<population[9].price<<endl;
    if(i==200) cout<<"200th generation: "<<population[0].price<<"   "<<population[9].price<<endl;



   }



}

};





int main(){
  int capacity;
  cout<<"Enter capacity: ";
  cin>>capacity;
  int numObjects;
  cout<<"Enter number of objects: ";
  cin>>numObjects;
  vector<int> price;
  vector<int> weight;
  price.resize(numObjects);
  weight.resize(numObjects);
  cout<<"Enter objects: "<<endl;
  cout<<"price  weight"<<endl;
  for(int i=0;i<numObjects;i++){
    cin>>price[i];
    cin>>weight[i];
  }
  cout<<"Everything is entered!"<<endl;
  Knapsack k(capacity,numObjects,price,weight);
  k.solve();



return 0;
}
