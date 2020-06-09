print("Welcome to Rune v1.0.0")

def show_license(short = true):
  if short:
    print("""
        Copyright (C) 2020 redstone2010


        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU Affero General Public License as published
        by the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.


        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU Affero General Public License for more details.


        You should have received a copy of the GNU Affero General Public License
        along with this program.  If not, see <https://www.gnu.org/licenses/>.
    """)
  else:
    print("Please see the LICENSE file included with Rune.")
    
print("What do you want to do?")
print(" > Start a new Rune project (press 1)")
print("   Create a new Rune project, either from scratch or from a template.")
print(" > Clone a Git repository into Rune (press 2)")
print("   You can also clone a Git repository containing a .runeconfig.yml file into Rune.")
print(" > Import an existing Rune project (press 3)")
print("   Work on an existing Rune project on your computer.")
print()
action = input()
if action == "1":
  print("Initializing...")
elif action == "2":
  print("Enter the path of the Git repository.")
elif action == "3":
  print("Enter the path of the Rune project.")
