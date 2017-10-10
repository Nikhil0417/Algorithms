//-----------Author: Sai Nikhil Reddy Mettupally------------------
//-----------Date of Creation: 02/28/2017-----------------------

#include<iostream>
#include<fstream>

using namespace std;
int var_count = 0;

void swap(int* x, int* y)	//function for swapping elements
{
	int t = *x;
	*x = *y;
	*y = t;
}

int partition(int a[], int left, int right)	//function for partitioning the array
{
	int pivot = a[right];	//pivot
	int i = (left-1);

	for (int j=left; j<=right-1;j++)
	{
		if (a[j] <= pivot)
		{
			i++;
			swap(&a[i], &a[j]);
			var_count++;
		}
		else
		{
			var_count++;
		}
	}
	swap(&a[i+1], &a[right]);
	return (i+1);
}

void quickSort(int a[], int left, int right)	//function for implementing quicksort
{
	if (left < right)
	{
		//var_count++;
		int p = partition(a, left, right);

		quickSort(a, left, p-1);
		quickSort(a, p+1, right);
	}
	/*else
	{
		var_count++;
	}*/
}

//--------------------MAIN PROGRAM---------------------

int main()
{
//--------------------METHOD-1-------------------------
	std::fstream myFile("input.txt");	//reading the file
	int r, c, i, j;

	myFile >> r >> c;	//reading the no. of rows and columns
	int a[10000];

	for (i=0;i<(r*c);i++)
	{
			myFile >> a[i];	//reading the elements in the file
	}

	quickSort(a, 0, ((r*c)-1) );

	/*for(i=0;i<(r*c);i++)
	{
		cout << a[i] << " ";
	}
	
	cout << endl;*/

	/*for(j=0;j<r;j++)
	{
		for(i=0;i<c;i++)
		{
			cout << a[(c*j) + i] << "\t";
		}
		cout << endl;
	}*/

	std::ofstream outputFile("sm0143_1.txt");

	for(j=0;j<r;j++)
	{
		for(i=0;i<c;i++)
		{
			outputFile << a[(c*j) + i] << "\t";
		}
		outputFile << endl;
	}
	outputFile << "no. of comparisons = " << var_count << endl;
	outputFile.close();

//--------------------METHOD-2---------------------

	var_count = 0;
	std::fstream myFile2("input.txt");	//reading the file

	myFile2 >> r >> c;	//reading the no. of rows and columns
	int b[100][100];
	int trans[100][100];

		for (i=0;i<r;i++)
		{
			for (j=0;j<c;j++)
			{
				myFile2 >> b[i][j];	//reading the elements in the file
				//cout << b[i][j] <<" ";
			}
			//cout << "\n";
		}
		//cout << "\n";

		for (i=0;i<r;i++)
		{
			quickSort(b[i], 0, c-1);	//sorting rows
		}

//-------------transpose code------------------
		for (i=0;i<r;i++)
		{
			for (j=0;j<c;j++)
			{
				trans[j][i] = b[i][j];
			}
		}
//---------------------------------------------

		/*for (i=0;i<c;i++)
		{
			for (j=0;j<r;j++)
			{
				cout << trans[i][j] << "\t";
			}
			cout << "\n";
		}
		cout << "\n";*/

		for (i=0;i<c;i++)
		{
			quickSort(trans[i], 0, r-1);	//sorting columns
		}

		/*for (i=0;i<c;i++)
		{
			for (j=0;j<r;j++)
			{
				cout << trans[i][j] << "\t";
			}
			cout << "\n";
		}
		cout << "\n";*/

//-----------inverse-transpose code-------------
		for (i=0;i<c;i++)
		{
			for (j=0;j<r;j++)
			{
				b[j][i] = trans[i][j];
			}
		}
//----------------------------------------------
//-----------printing the sorted matrix---------
		/*for (i=0;i<r;i++)
		{
			for (j=0;j<c;j++)
			{
				cout << b[i][j] <<"\t";
			}
			cout << "\n";
		}*/
	
	std::ofstream outputFile2("sm0143_2.txt");

	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			outputFile2 << b[i][j] << "\t";
		}
		outputFile2 << endl;
	}
	outputFile2 << "no. of comparisons = " << var_count << endl;
	outputFile2.close();

	//getchar();
	cout << "The output files have been generated. Please check..." << endl;
	return 0;
}
