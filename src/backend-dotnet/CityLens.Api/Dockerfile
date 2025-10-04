# src/backend-dotnet/CityLens.Api/Dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["CityLens.Api/CityLens.Api.csproj", "CityLens.Api/"]
RUN dotnet restore "CityLens.Api/CityLens.Api.csproj"
COPY . .
WORKDIR /src/CityLens.Api
RUN dotnet publish -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "CityLens.Api.dll"]
