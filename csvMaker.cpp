// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <sstream>
using namespace std;

int main () {
  string line;

  std::list<string> playerList;
  vector<string> aarray;

  ifstream myfile ("cfl_roster.csv");
  if (myfile.is_open())
  {
    while (getline (myfile,line))
    {
        cout<<line<<endl;
        for (int i=0; i<line.length(); i++)
        {
            if (line[i] == ',')
                line[i] = ' ';
        }

        stringstream ss(line);
        string temp;
        while (ss >> temp){
            aarray.push_back(temp);
            cout<<temp<<endl;
    }
    myfile.close();
  }
}
  else cout << "Unable to open file";



  return 0;
}
