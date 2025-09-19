from django.shortcuts import render
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class user_list_api(GenericAPIView):
    def get(self,request):
        users_objs = UserProfile.objects.filter(is_active=True).order_by('name')
        if users_objs.exists():
            serializer = UserProfileSerializer(users_objs,many=True)
            return Response({
                "data" : serializer.data,
                "response":{
                    "n":1,
                    "msg":"Users found Successfully",
                    "status":"success"
                    }
            })
        else:
            return Response({
                "data" : [],
                "response":{
                    "n":0,
                    "msg":"No Users Found",
                    "status":"error"
                    }
            })
        
class add_user_api(GenericAPIView):
    def post(self,request):
        print("request.data",request.data)
        data={}
        data['name']=request.data.get('name')
        data['mobile_number']=request.data.get('mobile_number')
        data['age']=request.data.get('age')
        data['email']=request.data.get('email')
        data['qualification']=request.data.get('qualification')
        print("data",data)
        if not data['name'] or not data['mobile_number'] or not data['age']:
            return Response({
                "data" : [],
                "response":{
                    "n":0,
                    "msg":"All fields are required",
                    "status":"error"
                    }
            })

        if UserProfile.objects.filter(mobile_number=data['mobile_number'],is_active=True).exists():
            return Response({
                "data" : [],
                "response":{
                    "n":0,
                    "msg":"Mobile Number already exists",
                    "status":"error"
                    }
            })


        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data" : serializer.data,
                "response":{
                    "n":1,
                    "msg":"User Added Successfully",
                    "status":"success"
                    }
            })
        else:
            print("serializer.errors",serializer.errors)
            return Response({
                "data" : [],
                "response":{
                    "n":0,
                    "msg":serializer.errors,
                    "status":"error"
                    }
            })

class get_user_detail_api(GenericAPIView):
    def get(self,request,pk):
        if pk:
            user_obj = UserProfile.objects.filter(pk=pk,is_active=True).first()
            if user_obj:
                serializer = UserProfileSerializer(user_obj)
                return Response({
                    "data" : serializer.data,
                    "response":{
                        "n":1,
                        "msg":"User found Successfully",
                        "status":"success"
                        }
                })
            else:
                return Response({
                    "data" : [],
                    "response":{
                        "n":0,
                        "msg":"No User Found",
                        "status":"error"
                        }
                })
        else:
            return Response({
                "data" : [],
                "response":{
                    "n":0,
                    "msg":"Please provide valid user id",
                    "status":"error"
                    }
            })


class edit_user_api(GenericAPIView):
    def put(self,request,pk):
        if pk:
            user_obj = UserProfile.objects.filter(pk=pk,is_active=True).first()
            if user_obj:
                data={}
                data['name']=request.data.get('name')
                data['mobile_number']=request.data.get('mobile_number')
                data['age']=request.data.get('age')
                data['email']=request.data.get('email')
                data['qualification']=request.data.get('qualification')



                if not data['name'] or not data['mobile_number'] or not data['age']:
                    return Response({
                        "data" : [],
                        "response":{
                            "n":0,
                            "msg":"All fields are required",
                            "status":"error"
                            }
                    })
                if UserProfile.objects.filter(mobile_number=data['mobile_number'],is_active=True).exclude(pk=pk).exists():
                    return Response({
                        "data" : [],
                        "response":{
                            "n":0,
                            "msg":"Mobile Number already exists",
                            "status":"error"
                            }
                    })
                print("data",data)

                serializer = UserProfileSerializer(user_obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        "data" : serializer.data,
                        "response":{
                            "n":1,
                        "msg":"User edited Successfully",
                        "status":"success"
                        }
                    })
                else:
                    return Response({
                        "data" : [],
                        "response":{
                            "n":0,
                            "msg":serializer.errors,
                            "status":"error"
                            }
                    })
            else:
                return Response({
                    "data" : [],
                    "response":{
                        "n":0,
                        "msg":"No User Found",
                        "status":"error"
                        }
                })
        else:
            return Response({
                "data" : [],
                "response":{
                    "n":0,
                    "msg":"Please provide valid user id",
                    "status":"error"
                    }
            })
      
   

class delete_user_api(GenericAPIView):
    def delete(self,request,pk):
        if pk:
            user_obj = UserProfile.objects.filter(pk=pk,is_active=True).first()
            if user_obj:
                data={}
                data['is_active']=False
                serializer = UserProfileSerializer(user_obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        "data" : serializer.data,
                        "response":{
                            "n":1,
                        "msg":"User deleted Successfully",
                        "status":"success"
                        }
                    })
                else:
                    return Response({
                        "data" : [],
                        "response":{
                            "n":0,
                            "msg":serializer.errors,
                            "status":"error"
                            }
                    })
            else:
                return Response({
                    "data" : [],
                    "response":{
                        "n":0,
                        "msg":"No User Found",
                        "status":"error"
                        }
                })
        else:
            return Response({
                "data" : [],
                "response":{
                    "n":0,
                    "msg":"Please provide valid user id",
                    "status":"error"
                    }
            })
      










